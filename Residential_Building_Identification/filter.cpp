// This code will open the GeoJSON file, read the
// contents into a string, and then parse the 
// string into a RapidJSON document object. It
// will then iterate through the features in the
// document and extract the coordinates for each
// feature. Finally, it will print the coordinates
// to the screen.

// Note that this code assumes that the GeoJSON 
// file follows the standard format for a GeoJSON
// file, with a top-level features property that
// contains an array of feature objects. Each 
// feature object should have a geometry property
// that contains the coordinates for the feature.

#include <iostream>
#include <fstream>
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

using namespace rapidjson;
using namespace std;

int main() {
    // Open the GeoJSON file
    ifstream infile("buildings.geojson");
    stringstream buffer;
    buffer << infile.rdbuf();
    string contents(buffer.str());

    // Parse the JSON document
    Document document;
    document.Parse(contents.c_str());

    // Set the bounding box for the area of interest
    double min_lat = 40.7;
    double max_lat = 40.8;
    double min_lng = -74.0;
    double max_lng = -73.9;

    // Create an array to store the filtered features
    Value filtered_features(kArrayType);

    // Iterate through the features in the GeoJSON file
    for (SizeType i = 0; i < document["features"].Size(); i++) {
        // Get the coordinates of the current feature
        const Value& coordinates = document["features"][i]["geometry"]["coordinates"];
        // Check if the coordinates fall within the bounding box
        if (coordinates[1].GetDouble() >= min_lat && coordinates[1].GetDouble() <= max_lat && coordinates[0].GetDouble() >= min_lng && coordinates[0].GetDouble() <= max_lng) {
            // Add the feature to the filtered array
            filtered_features.PushBack(document["features"][i], document.GetAllocator());
        }
    }

    // Write the filtered features to a new GeoJSON file
    ofstream outfile("filtered_buildings.geojson");
    StringBuffer s;
    Writer<StringBuffer> writer(s);
    writer.StartObject();
    writer.Key("type");
    writer.String("FeatureCollection");
    writer.Key("features");
    writer.StartArray();
    for (SizeType i = 0; i < filtered_features.Size(); i++) {
        filtered_features[i].Accept(writer);
    }
    writer.EndArray();
    writer.EndObject();
    outfile << s.GetString();
    outfile.close();

    return 0;
}
