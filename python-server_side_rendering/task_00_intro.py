def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # Check if all items in attendees list are dictionaries
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data
        processed_template = template
        
        # Define the placeholders to replace
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        for placeholder in placeholders:
            placeholder_key = f"{{{placeholder}}}"
            value = attendee.get(placeholder)
            
            # If value is None or missing, replace with "N/A"
            if value is None:
                value = "N/A"
            
            processed_template = processed_template.replace(placeholder_key, str(value))
        
        # Generate output file
        output_filename = f"output_{index}.txt"
        
        try:
            with open(output_filename, 'w') as file:
                file.write(processed_template)
            print(f"Generated {output_filename}")
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")