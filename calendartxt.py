import csv
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta

def read_txt_and_create_ics(txt_file, ics_file, delimiter=','):
    # Open the text file for reading
    with open(txt_file, 'r', newline='', encoding='utf-8') as txtfile:
        lines = txtfile.readlines()
        print(lines)

        
        # Create a new iCalendar object
        cal = Calendar()

        # Skip header row if present (optional)
        lines = lines[1:]
        print('lines', lines)

    

        # Iterate over each line in the text file
        for line in lines:
            print('lines', lines)
            # Split line into columns based on the delimiter
            row = line.strip().split(delimiter)
            print("hi",row)
            
            # Extract data from text line
            event_name = row[0]
            start_date_str = row[1]

            # Parse dates from strings
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

            # Create a new event
            event = Event()
            event.add('summary', event_name)
            event.add('dtstart', start_date)

            # Add event to the calendar
            cal.add_component(event)

            # Create a VALARM for the event
            alarm = Alarm()
            alarm.add('action', 'DISPLAY')
            alarm.add('description', f'Reminder: {event_name} in 1 day')
            alarm.add('trigger', timedelta(days=-1))  # Trigger 1 day before event
            event.add_component(alarm)

    # Write the iCalendar data to a file
    with open(ics_file, 'wb') as f:
        f.write(cal.to_ical())

# Example usage:
read_txt_and_create_ics('C:\\Users\\gurpreet_kaur\\Downloads\\calendar.txt', 'C:\\Users\\gurpreet_kaur\\Downloads\\calendar.ics')
