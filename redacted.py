def redact_entities(input_text, entity_map):
    redacted_text = input_text
    placeholder_map = {}
    
    for i in entity_map:
            # Generate a unique placeholder for each entity
            placeholder = f"{i[0]}{len(placeholder_map) + 1}"
            placeholder_map[placeholder] = i[1]
            
            # Replace the entity with the placeholder in the redacted text
            redacted_text = redacted_text.replace(i[1], placeholder)
    
    return redacted_text, placeholder_map


# User input for text
def inputs(input_text,entity_input):
    # input_text = input("Enter the text: ")

# User input for entities as a comma-separated list of key-value pairs
    # entities_input = input("Enter entities (e.g., Name: Bard, Organisation: Google AI): ")
    # entity_pairs = [entity.strip() for entity in entity_input.split(",")]
    # entity_map = {}

    # for entity_pair in entity_pairs:
    #     key, value = [item.strip() for item in entity_pair.split(":")]
    # # Check if the entity type already exists in the map
    #     if key in entity_map:
    #         entity_map[key].append(value)
    #     else:
    #         entity_map[key] = [value]

# Redact the text based on user input
    redacted_text, placeholder_map = redact_entities(input_text, entity_input)
    return redacted_text,placeholder_map
# Print the redacted text and placeholder map
    # print("\nRedacted Text:")
    # print(redacted_text)
    # print("\nPlaceholder Map:")
    # for placeholder, original_value in placeholder_map.items():
    #     print(f"{placeholder}: {original_value}")

