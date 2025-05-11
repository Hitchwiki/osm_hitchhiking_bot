from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task

def edit_element(tags):
    if "amenity" not in tags.keys():
        tags.pop('highway', None)
        tags["highway"] = "hitchhiking"
    
    if "amenity" in tags.keys() and tags["amenity"] == "bench":
        tags.pop('highway', None)
        tags.pop('amenity', None)
        tags["highway"] = "hitchhiking"
        tags["bench"] = "yes"

    if "amenity" in tags.keys() and tags["amenity"] == "car_pooling":
        tags.pop('highway', None)
        tags.pop('amenity', None)
        tags["highway"] = "hitchhiking"

    if "amenity" in tags.keys() and tags["amenity"] == "shelter":
        tags.pop('highway', None)
        tags.pop('amenity', None)
        tags["highway"] = "hitchhiking"
        tags["shelter"] = "yes"
    
    return tags

highway_hitchhiking_bench_download = """
/*

*/
[out:xml][timeout:25];
// gather results
nwr["highway"="hitchhiking_bench"];
// print results
out geom;
"""

def main():
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=500,
        objects_to_consider_query=highway_hitchhiking_bench_download,
        cache_folder_filepath='./cache',
        is_in_manual_mode=False,
        changeset_comment='Replacing undocumented and redundant highway=hitchhiking_bench tag with highway=hitchhiking. Also mapping amenity=bench like for highway=bus_stop.',
        discussion_url='https://wiki.openstreetmap.org/wiki/Talk:Mechanical_Edits/TillWenke/moving_hitchhiking_stops_to_%27highway%3Dhitchhiking%27_(mainly_in_Europe/Germany)',
        osm_wiki_documentation_page='https://wiki.openstreetmap.org/wiki/Mechanical_Edits/TillWenke/moving_hitchhiking_stops_to_%27highway%3Dhitchhiking%27_(mainly_in_Europe/Germany)',
        edit_element_function=edit_element,
    )

main()