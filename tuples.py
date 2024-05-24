def get_coordinate(record):
    return record[1]


"""Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
"""



def convert_coordinate(coordinate):
    new_format=coordinate[0],coordinate[1]
    return new_format
    
        
        
    return new_format

"""Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
"""




def create_record(azara_record, rui_record):
    join_coordinate=""
    for i in rui_record[1]:
        join_coordinate+=i
    if azara_record.count(join_coordinate)==1:
        return azara_record+rui_record
    else:
        return "not a match"
