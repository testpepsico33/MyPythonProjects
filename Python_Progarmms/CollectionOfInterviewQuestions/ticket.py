def generate_ticket_id(ticket_info):
    parts = ticket_info.split(':')
    if len(parts) != 2:
        return ""  # Invalid format

    source = parts[0]
    mobile_number = parts[1]

    # Extract first two characters of source
    source_prefix = source[:2]

    # Calculate sum of digits at even indices (including 0)
    even_index_sum = 0
    for i in range(0, len(mobile_number), 2):
        if mobile_number[i].isdigit():
            even_index_sum += int(mobile_number[i])

    # Generate sequence number (assuming it's always 1 as per the note)
    sequence_number = "1"

    # Combine to form the ticket ID
    ticket_id = source_prefix + str(even_index_sum) + sequence_number
    return ticket_id

if __name__ == "__main__":
    input_string = input()
    passenger_tickets = input_string.split(',')
    output_ids = []

    for i, ticket in enumerate(passenger_tickets):
        ticket_id = generate_ticket_id(ticket.strip())
        if ticket_id:
            output_ids.append(ticket_id)

    print(','.join(output_ids))

