import pandas as pd
import numpy as np
import csv

def sqlite_to_df_cl4_pc(db):
    # Defining the keys outside of the loop
    I_keys = [f"I{_}" for _ in range(1, 56)]
    N_keys = [f"N{_}" for _ in range(1, 22)]
    keys = ['space_dim', 'homology_dim', 'num_pts',\
             'critical_radii_number','ladder_length','dots','lines']
    rows = []
    for record in db.get_all():
        info=record.info
        row = {key: info.get(key) for key in keys}
        row |= {'num_pts_removal': len(info['vertical_removal'])}
        row |= {key: info['decomp'].get(key, 0) for key in I_keys + N_keys}
        rows.append(row)
    df = pd.DataFrame(rows)
    return df


def sqlite_to_df_cln_pc(db):
    # Defining the keys outside of the loop
    keys = ['space_dim', 'homology_dim', 'num_pts',\
             'critical_radii_number','ladder_length','dots','lines']
    rows = []
    for record in db.get_all():
        info = record.info
        row = {key: info.get(key) for key in keys}
        row |= {'num_pts_removed': len(info['vertical_removal'])}
        # data_str_lines=record.info['lines']
        # data_str_dots=record.info['dots']
        # lines = data_str_lines.strip().split('\n')
        # dots = data_str_dots.strip().split('\n')
        # reader_lines = csv.DictReader(lines)
        # reader_dots = csv.DictReader(dots)
        # multiplicity_values_lines = np.array([int(row['multiplicity']) for row in reader_lines],dtype=np.int32)
        # multiplicity_values_dots = np.array([int(row['multiplicity']) for row in reader_dots],dtype=np.int32)
        # # store the numpy arrays
        # row |= {'multiplicity_values_lines': multiplicity_values_lines}
        # row |= {'multiplicity_values_dots': multiplicity_values_dots}
        rows.append(row)
    df = pd.DataFrame(rows)
    return df



# def sqlite_to_df_cln(db):
#     rows = []
#     for record in db.get_all():
#         space_dim = record.info['space_dim']
#         try:
#             homology_dim = record.info['homology_dim']
#         except:
#             homology_dim = record.info['homological_dim']
#         num_pts = record.info['num_pts']
#         num_pts_removed = len(record.info['vertical_removal'])
#         ladder_length = len(record)
#         data_str_lines=record.info['lines']
#         data_str_dots=record.info['dots']
#         lines = data_str_lines.strip().split('\n')
#         dots = data_str_dots.strip().split('\n')
#         reader_lines = csv.DictReader(lines)
#         reader_dots = csv.DictReader(dots)
#         multiplicity_values_lines = [int(row['multiplicity']) for row in reader_lines]
#         #get the sum of positive multiplicities and negative multiplicities separately
#         #using only one loop
#         sum_positive_lines = 0
#         sum_negative_lines = 0
#         for multiplicity in multiplicity_values_lines:
#             if multiplicity >= 0:
#                 sum_positive_lines += multiplicity
#             else:
#                 sum_negative_lines += multiplicity
#         multiplicity_values_dots = [int(row['multiplicity']) for row in reader_dots]
#         sum_dots = 0
#         for multiplicity in multiplicity_values_dots:
#             if multiplicity >= 0:
#                 sum_dots += multiplicity
#             else:
#                 raise ValueError('Negative multiplicity found in dots.')
#         row_dict = {'space_dim': space_dim,
#                     'homology_dim': homology_dim,
#                     'num_pts': num_pts,
#                     'num_pts_removed': num_pts_removed,
#                     'ladder_length': ladder_length,
#                     'multiplicity_positive_dots': sum_dots,
#                     'multiplicity_positive_lines': sum_positive_lines,
#                     'multiplicity_negative_lines': sum_negative_lines}
#         rows.append(row_dict)
#     df = pd.DataFrame(rows)
#     return df