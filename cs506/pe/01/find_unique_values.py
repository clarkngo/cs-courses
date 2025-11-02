from typing import List, Dict, Any, Set

def find_unique_values(data: List[Dict[str, Any]]) -> Set[Any]:
    """
    Extracts all unique values from a list of single-key-value dictionaries.
    """
    unique_values = set()
    
    for d in data:
        # The values() method returns a list-like view of the dictionary's values.
        # Since each dictionary has only one key-value pair, the first element 
        # of the values() view is the value we need.
        # Using d.values() is robust regardless of the key name.
        value = next(iter(d.values()))
        unique_values.add(value)
            
    return unique_values

# Sample Data:
sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
               {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_set = find_unique_values(sample_data)
print(f"Unique Values: {unique_set}")
# Expected Output: Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
