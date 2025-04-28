import scanpy as sc

adata = sc.read_h5ad("nCoV_dataset.h5ad")


print(adata)

print(adata.obs.head())

print(adata.obsm.keys())

