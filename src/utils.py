from anndata import AnnData

def observe_condition(adata: AnnData):
    batch_to_condition = {
        0: "Ctrl-1",
        1: "Ctrl-2",
        2: "Ctrl-3",
        3: "IAV-1-D1",
        4: "IAV-1-D14",
        5: "IAV-2-D1",
        6: "IAV-2-D9",
        7: "COV-1-D1",
        8: "COV-1-D4",
        9: "COV-1-D16",
        10: "COV-2-D1",
        11: "COV-2-D4",
        12: "COV-2-D7",
        13: "COV-2-D10",
        14: "COV-2-D16",
        15: "COV-3-D1",
        16: "COV-3-D4",
        17: "COV-3-D16",
        18: "COV-4-D4",
        19: "COV-4-D16",
        20: "COV-5-D1",
        21: "COV-5-D7",
        22: "COV-5-D13",
    }

    adata.obs["sample_name"] = adata.obs["batch"].map(batch_to_condition)

    def categorize(sample: str):
        if sample.startswith("Ctrl"):
            return "Control"
        elif sample.startswith("COV"):
            return "COVID"
        elif sample.startswith("IAV"):
            return "IAV"
        else:
            return "Unknown"

    adata.obs["condition"] = adata.obs["sample_name"].apply(categorize)

def observe_cell_types(adata: AnnData):
    cell_type_mapping = {
        0: "Cytotoxic CD8 T cells",
        1: "Naive T cells",
        2: "NKs",
        3: "MAIT",
        4: "Activated CD4 T cells",
        5: "Naive B cells",
        6: "Plasma",
        7: "Memory B cells",
        8: "XCL+ NKs",
        9: "Cycling T cells",
        10: "Monocytes",
        11: "DCs",
        12: "Cycling Plasma",
        13: "Stem cells",
        14: "Megakaryocytes",
    }

    adata.obs["cell_type_name"] = adata.obs["cell_type"].map(cell_type_mapping)
