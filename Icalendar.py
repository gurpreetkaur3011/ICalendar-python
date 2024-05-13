import csv
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta

def read_csv_and_create_ics(csv_file, ics_file):
    # Open the CSV file for reading
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if present
        
        # Create a new iCalendar object
        cal = Calendar()

        # Iterate over each row in the CSV file
        for row in csvreader:
            # Extract data from CSV row
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
read_csv_and_create_ics('C:\\Users\\gurpreet_kaur\\Downloads\\events.csv', 'C:\\Users\\gurpreet_kaur\\Downloads\\calendar.ics')
