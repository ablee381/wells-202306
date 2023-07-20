from vega_datasets import data
import altair as alt
import pandas as pd


def plot_wells(well_coords):
    states = alt.topo_feature(data.us_10m.url, feature='states')
    USmap = alt.Chart(states) \
        .mark_geoshape(fill='lightgray', stroke='white') \
        .project('albersUsa') \
        .properties(width=500, height=300)
    # Add the wells information to map
    columns = ['latitude', 'longitude', 'depth', 'gradient']
    well_coords = pd.DataFrame(well_coords, columns=columns)

    well_coordinates = (alt.Chart(well_coords)
                        .mark_circle()
                        .encode(latitude='latitude',
                                longitude='longitude',
                                color=alt.Color('gradient', title='Gradient',
                                                scale=alt.Scale(scheme='inferno')),
                                tooltip=[alt.Tooltip('depth', title='Depth (m)'),
                                         alt.Tooltip('gradient', title='Gradient (C/m)',
                                                     format='0.2f')])
                        )
    return USmap + well_coordinates


if __name__ == '__main__':
    from database import query_db

    results = query_db(1500, 0.1)
    plot_wells(results).save('test.png')
