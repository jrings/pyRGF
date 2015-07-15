"""Train and predict with RGF"""

import tempfile

def sanity_check_train(p):
    """Checks that all training parameters are legal
    """
    if not isinstance(p, dict):
        raise ValueError("Training params must be a dict")
    legal_keys = ["algorithm", "loss", "max_leaf_forest", "normalize_target",
    "reg_l2", "reg_sl2", "reg_depth", "test_interval", "min_pop",
    "num_iteration_opt", "num_tree_search", "opt_interval",
    "opt_stepsize", "verbose", "time", "memory_policy"]

    if not set(legal_keys).issuperset(set(p.keys())):
        illegal_keys = set(p.keys())-set(legal_keys)
        raise KeyError(
            "Training params contains illegal keys {}".format(illegal_keys))

    assert p.get("algorithm", "RGF") in ["RGF", "RGF_Opt", "RGF_Sib"]
    assert p.get("loss", "LS") in ["LS", "Expo", "Log"]
    

def train(df, params={}):
    """Train RGF with DataFrame df and parameters in param
    """

    sanity_check_train(params)
    with tempfile.TemporaryFile(suffix=".in") as _c:
        for k, v in p.items():
            if k == "normalize_target" and v:
                print("NormalizeTarget", file="_c")
            elif k == "verbose" and v:
                print("Verbose", file="_c")
            elif k == "time" and v:
                print("Time", file="_c")
            else:
                print("{}={}".format(k, v))
        
                