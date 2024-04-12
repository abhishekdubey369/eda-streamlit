from data import DataOp as CleanOp
from sidebar import sidebarClean
import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv(f"F:\ml\TF_GPU_Conda_env_Dockerfile\TF_GPU_Conda_env_Dockerfile\sales\Amazon Sale Report.csv\Amazon Sale Report.csv")
    cond = sidebarClean()
    CleanOp(data, cond)

if __name__ == "__main__":
    main()
