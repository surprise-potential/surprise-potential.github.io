import numpy as np


dataset_name = "nuplanmini"  # nuscenes, waymo, nuplanmini
split = "val"  # train, val

score_path = f"./{dataset_name}/{dataset_name}_{split}.npy"
score = np.load(score_path, allow_pickle=True).item()

print(len(score["dist"]))
