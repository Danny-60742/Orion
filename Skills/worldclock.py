from datetime import datetime
from zoneinfo import ZoneInfo

# Cities Orion knows

TIME_ZONES = {
        "lagos": "Africa/Lagos",
        "nigeria": "Africa/Lagos",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
        "new york": "America/New_York",
        "los angeles": "America/Los_Angeles",
        "chicago": "America/Chicago",
        "paris": "Europe/Paris",
        "dubai": "Asia/Dubai",
        "beijing": "Asia/Shanghai",
        "denver": "America/Denver",
        "toronto": "America/Toronto",
        "winnipeg": "America/Winnipeg",
        "edmonton": "America/Edmonton",
        "vancouver": "America/Vancouver",
        "sydney": "Australia/Sydney",
        "adelaide": "Australia/Adelaide",
        "perth": "Australia/Perth",
 }
MULTI_ZONE_COUNTRIES = {
        "usa": ["new york", "chicago", "denver", "los angeles"],
        "canada": ["toronto", "winnipeg", "edmonton", "vancouver"],
        "australia": ["sydney", "adelaide", "perth"]
 }

def get_world_time(place):
         place = place.lower()

         if place in MULTI_ZONE_COUNTRIES:
              cities = MULTI_ZONE_COUNTRIES[place]

              message = f"{place.title()} has multiple time zones.\n"
              message += "Choose one of these cities:\n"

              for city in cities:
                  message += f"- {city.title()}\n"

              return message
                                                                                                    # 👇 Then continue with your normal city lookup
         if place in TIME_ZONES:
              zone = ZoneInfo(TIME_ZONES[place])
              current_time = datetime.now(zone)
              return f"The current time in {place.title()} is {current_time.strftime('%H:%M:%S')}"
              
              return "Sorry, I don't know that location yet."
