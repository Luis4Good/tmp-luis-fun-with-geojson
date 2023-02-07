"""_summary_

Returns:
    generates a geojson file with only MultiPolygons
"""

import json


def read_geojson(path):
    with open(path, 'r') as f:
        geojson = json.load(f)
    return geojson

def read_features_from_geojson(path):
    geojson = read_geojson(path)
    return geojson['features']

def force_feature_to_multipolygon(feature):
    if feature['geometry']['type'] == 'Polygon':
        feature['geometry']['type'] = 'MultiPolygon'
        feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]
    return feature


# def count_numbers_of_features(features):
#     return len(features)

def save_geojson(path, geojson):
    with open(path, 'w') as f:
        json.dump(geojson, f )

def main():
    features = read_features_from_geojson('./allplots_2022-12.geojson')
    for feature in features:
        feature = force_feature_to_multipolygon(feature)
    save_geojson('./OnlyMultiPolygons.geojson', {'type': 'FeatureCollection', 'features': features})
    # print(f"number of features: {count_numbers_of_features(features)}")


if __name__ == '__main__':
    main()