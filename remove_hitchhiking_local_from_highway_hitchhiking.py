from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task


def edit_element(tags):
    if "amenity" not in tags.keys() and "highway" in tags.keys() and "hitchhiking" in tags.keys():
        tags.pop('hitchhiking', None)
    
    return tags

hitchhiking_local_download = """
/*

*/
[out:xml][timeout:25];
// gather results
nwr["hitchhiking"="local"];
// print results
out geom;
"""

def main():
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=500,
        objects_to_consider_query=hitchhiking_local_download,
        cache_folder_filepath='./cache',
        is_in_manual_mode=True,
        changeset_comment='Removing undocumented and redundant hitchhiking=local tag from highway=hitchhiking nodes.',
        discussion_url='https://wiki.openstreetmap.org/wiki/Talk:Mechanical_Edits/TillWenke/moving_hitchhiking_stops_to_%27highway%3Dhitchhiking%27_(mainly_in_Europe/Germany)',
        osm_wiki_documentation_page='https://wiki.openstreetmap.org/wiki/Mechanical_Edits/TillWenke/moving_hitchhiking_stops_to_%27highway%3Dhitchhiking%27_(mainly_in_Europe/Germany)',
        edit_element_function=edit_element,
    )

main()