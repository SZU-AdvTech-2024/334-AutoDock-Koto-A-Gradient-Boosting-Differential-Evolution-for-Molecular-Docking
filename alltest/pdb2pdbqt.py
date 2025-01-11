import os
base_path = "/root/alltest"  # 替换为实际的文件路径

file_names = [ ["1bzc"], ["1c5z"], ["1e66"], ["1eby"], ["1g2k"], ["1gpk"], ["1gpn"], ["1h22"],
              ["1h23"], ["1k1i"], ["1lpg"], ["1mq6"], ["1nc1"], ["1nc3"], ["1nvq"], ["1o0h"], ["1o3f"], ["1o5b"]]

total_files = len(file_names)
for i in range(total_files):
    input_file = os.path.join(base_path, file_names[i][0] + "_ligand.mol2")
    output_file = os.path.join(base_path, file_names[i][0] + "_ligand.pdb")
    cmd = f"obabel {input_file} -O {output_file}"
    os.system(cmd)

