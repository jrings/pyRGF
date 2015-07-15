"""Converts pandas DataFrames to and from
RGF format
"""

import pandas as pd


def convert_to_rgf(
        df, fname_prefix, response_column=None, verbose=True,
        exclude_columns=None):
    """Takes the pandas DataFrame df and stores it in RGF format
    in fname_prefix.x and fname_prefix.y (if response_column is set)
    Parameters:

    * df <pd.DataFrame>: pandas DataFrame to convert
    * fname_prefix <str>: Filename prefix for output
    * response_column <str|None>: If set, use this for the target variable
    that is written to <fname_prefix>.y
    * verbose <bool|True>: Print a few status messages if True
    * exclude_columns <[str]|None>: Optionally a list of columns to exclude
    (Useful e.g. if an ID column is included)
    """
    df = df.copy()
    if response_column and response_column not in df:
        raise KeyError(
            "Response column {} not in DataFrame".format(response_column))
    if exclude_columns:
        for col in exclude_columns:
            if col not in df:
                raise KeyError(
                    "Column {} not in DataFrame".format(col))
            _ = df.pop(col)
            
    if response_column:
        y = list(df.pop(response_column))

        # For convenience, if data set is for classification but 0 and 1,
        # convert to -1 and 1
        if set([0, 1]) == set(y):
            y = [-1 if a == 0 else 1 for a in y]
        with open(fname_prefix + ".y", 'w') as _out:
            for a in y:
                print(a, file=_out)
        if verbose:
            print("Wrote response vector to {}".format(fname_prefix + ".y"))

    with open(fname_prefix + ".x", 'w') as _out:
        for row in df.itertuples():
            row = [str(a) for a in list(row)[1:]]
            print(" ".join(row), file=_out)
    if verbose:
        print("Wrote predictors to {}".format(fname_prefix + ".x"))



if __name__ == "__main__":
    print("Only usable as functions currently")

            
    