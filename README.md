# DSC210 Final Project -  Random Linear Algebra


## Instructions

### Random Linear Algebra for Matrix Multiplication and SVD

Codes for Random Matrix Multiplication and Random SVD are provided under `Algorithms`

### Random Linear Algebra for Efficient Parameter Updates

Codes is adopted from [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://github.com/UCDvision/NOLA/tree/main).

To install the environment
```
cd NOLA
pip install -r requirements.txt
```

To prepare the dataset:
```
# Download CIFAR-10 Dataset
cd NOLA
python download.py
```

To run the training and experiments
```
cd NOLA
python exp.py --exp [EXPERIMENT]
```
[EXPERIMENT] can be choosen from:
* "architecture": test different finetuning methods
* "rank": test LoRA and NOLA on different ranks
* "num_k": test NOLA with different number of basis

Graph from our report is created by after running "num_k" experiement, and the graph can be generated running `graph.py`