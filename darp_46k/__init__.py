import gzip
import numpy as np


number_of_agents = 4
number_of_obstacles = 10
map_rows = 10
packed_example_size = 64


def unpack_example(data, number_of_agents, number_of_obstacles, map_rows):

    final_array = bytes_to_bitstring(data)

    # Decode parameters...

    element_size = math.ceil(math.log2(map_rows))
    agent_positions_length = element_size * number_of_agents * 2
    agent_positions = []


    # Decode agent coordinates...

    for i in range(0, agent_positions_length, element_size * 2):
        x = int(final_array[i : i + element_size], 2)
        y = int(final_array[i + element_size : i + element_size * 2], 2)
        
        agent_positions.append((y, x))
    
    final_array = final_array[agent_positions_length :]


    # Decode obstacle coordinates...

    obstacle_positions = []
    number_of_obstacles = map_rows
    obstacle_positions_length = element_size * number_of_obstacles * 2

    for i in range(0, obstacle_positions_length, element_size * 2):

        x = int(final_array[i : i + element_size], 2)
        y = int(final_array[i + element_size : i + element_size * 2], 2)
        
        obstacle_positions.append((y, x))
    
    final_array = final_array[obstacle_positions_length :]


    # Finally, decode solutions

    solution = []
    area_length = (map_rows ** 2)

    for i in range(number_of_agents):
        area_array = final_array[i * area_length : (i + 1) * area_length]
        area_array = np.array([int(x) for x in area_array]).reshape(-1, map_rows)

        solution.append(area_array)

    solution = np.array(solution).astype('uint8')

    return (
        agent_positions,
        obstacle_positions,
        solution,
    )


def load_data():
    data = []
    
    with open('./dataset.gz', 'rb') as file:
        content = file.read()
        content = gzip.decompress(content)
        
        assert len(content) % packed_example_size == 0
        number_of_examples = len(content) // packed_example_size 
        
        for i in range(number_of_examples):
        
            example_packed = content[i * packed_example_size : (i + 1) * packed_example_size]
            example = unpack_example(example_packed, number_of_agents, number_of_obstacles, map_rows)
            
            data.append(example)
        
            if ((i + 1) % 10_000) == 0:
                print(f'Extracted {i+1}/{number_of_examples} examples.')
     
    return data
