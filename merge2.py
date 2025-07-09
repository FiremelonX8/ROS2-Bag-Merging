import ros2bag
import os

import ros2bag.verb
import ros2bag.verb.convert
com = ros2bag.verb.convert.ConvertVerb

os.mkdir('bags') if not os.path.exists('bags') else None

com = com()
# com.add_arguments('-i', None)
for i in os.listdir('bags'):
    for j in os.listdir(i):
        if j.endswith('.db3'):
            com.add_arguments('-i', [os.path.join('bags', i)])
            com.main()


"""def merge_bags(input_bag_paths, output_bag_path):
    
    Merge multiple ROS 2 bag files into a single bag file.
    
    :param input_bag_paths: List of paths to input bag files.
    :param output_bag_path: Path to the output merged bag file.
    
    with ros2bag.Bag(output_bag_path, 'w') as outbag:
        for bag_path in input_bag_paths:
            with ros2bag.Bag(bag_path, 'r') as inbag:
                for topic, msg, t in inbag.read_messages():
                    outbag.write(topic, msg, t)
    print(f"Merged {len(input_bag_paths)} bags into {output_bag_path}.")"""