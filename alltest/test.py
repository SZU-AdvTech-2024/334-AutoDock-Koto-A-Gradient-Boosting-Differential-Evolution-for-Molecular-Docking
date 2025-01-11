import subprocess


file_names = [ ["1bzc"], ["1c5z"], ["1e66"], ["1eby"], ["1g2k"], ["1gpk"], ["1gpn"], ["1h22"],
              ["1h23"], ["1k1i"], ["1lpg"], ["1mq6"], ["1nc1"], ["1nc3"], ["1nvq"], ["1o0h"], ["1o3f"], ["1o5b"]]

total_files = len(file_names)


for i in range(total_files):
    input_file = file_names[i][0] + "_ligand.mol2"
    output_file = file_names[i][0] + "_ligand.pdb"
    cmd = ["obabel", input_file, "-O", output_file]
    
    print("Running command:", " ".join(cmd))  # 打印命令
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")
    else:
        print(f"Successfully converted {input_file} to {output_file}")
