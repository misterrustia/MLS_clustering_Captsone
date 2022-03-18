import pandas as pd
import os
import pickle



def save_file(data, fname, dname):
    """Save a datafile (data) to a specific location (dname) and filename (fname)

    Currently valid formats are limited to CSV or PKL."""

    if not os.path.exists(dname):
        os.mkdir(dname)
        print(f'Directory {dname} was created.')

    fpath = os.path.join(dname, fname)


    if os.path.exists(fpath):
        print("A file already exists with this name.\n")

        yesno = None
        while yesno != "Y" and yesno != "N":
            yesno = input('Do you want to overwrite? (Y/N)').strip()[0].capitalize()
            if yesno == "Y":
                print(f'Writing file.  "{fpath}"')
                _save_file(data, fpath)
                break  # Not required
            elif yesno == "N":
                print('\nPlease re-run this cell with a new filename.')
                break  # Not required
            else:
                print('\nUnknown input, please enter "Y" or "N".')

    else:  # path does not exist, ok to save the file
        print(f'Writing file.  "{fpath}"')
        _save_file(data, fpath)






def _save_file(data, fpath):
    import pickle
    valid_ftypes = ['.csv', '.pkl']

    assert (fpath[-4:] in valid_ftypes), "Invalid file type.  Use '.csv' or '.pkl'"

    # Figure out what kind of file we're dealing with by name
    if fpath[-3:] == 'csv':
        data.to_csv(fpath, index=False)
    elif fpath[-3:] == 'pkl':
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)

            
def create_ranges(player1,player2,params, df):
    ranges = []
    a_values = []
    b_values = []


    # create ranges for each player
    for x in params:
        a = min(df[params][x])
        a = a - (a*.15)
        b = max(df[params][x])
        b = b + (b*.15)
        ranges.append((a,b,))

    for x in range(len(df['player_name'])):
        if df['player_name'].iloc[x] == player1:
            a_values = df.iloc[x].values.tolist()

        if df['player_name'].iloc[x] == player2:
            b_values = df.iloc[x].values.tolist()

    #remove names and club from values 
    a_values = a_values[2:]
    b_values = b_values[2:]

    values = [a_values,b_values]
    return values, ranges


def radar_compare(player1,player2,params, df):
    from soccerplots.radar_chart import Radar
    values, ranges = create_ranges(player1,player2, params, df)
    title = dict(
    title_name=player1,
    title_color = 'royalblue',
    subtitle_name = 'defensive stats',
    subtitle_color = 'orange',
    title_name_2=player2,
    title_color_2 = 'red',
    subtitle_name_2 = 'defensive stats',
    subtitle_color_2 = 'purple',
    title_fontsize = 18,
    subtitle_fontsize=8
    )

    ## endnote 
    endnote = "Visualization made by: Robert Rustia \nAll units are in per90 and are possesion adjusted"

    radar = Radar()

    fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                             radar_color=['orange','purple'],
                             alphas=[0.3,0.3],
                             title=title,
                             figsize = (20, 20),
                             compare=True,
    endnote = endnote
    )
    