import shutil

# Source and destination file paths
src_file = '/home/ali.zaidi/PycharmProjects/python_training/important_libraries/data.csv'
dst_file = '/home/ali.zaidi/PycharmProjects/python_training/sample_problems'

# Copy the source file to the destination
shutil.copy(src_file, dst_file)

print(f'Copied {src_file} to {dst_file}')

###################################################################################

#moving file

# Source and destination file paths
src_file = '/home/ali.zaidi/PycharmProjects/python_training/important_libraries/data.xlsx'
dst_file = '/home/ali.zaidi/PycharmProjects/python_training/sample_problems'

# Move the source file to the destination
shutil.move(src_file, dst_file)

print(f'Moved {src_file} to {dst_file}')

