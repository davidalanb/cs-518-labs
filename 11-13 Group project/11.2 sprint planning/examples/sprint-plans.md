# Sprint goal

Goal: "Enable guides and clients to create and discover adventures, respectively."
More specific goal: "Enable basic adventure creation and listing."
Stretch goal: "Enable adventure specification and discovery by datetime and/or location."

## Selected stories

Prioritize stories.  Come up with more if you need to.  Or decompose large stories as needed.
Each feature team (pair) should select a few higher-priority stories (definitely want to get done this sprint), and a few lower-priority stories (get to these if/when you finish the others).

* Feature 1: adventure creation

    * p::1.  As a guide, I want to specify a title and description for my adventure, so that..
    * p::2.  As a guide, I want to mark my adventure as a "Multi-day Trip" and input start/end dates, so that users have full clarity on the commitment required.
    * p::3.  As a guide, I want to specify location, so that..
    --
    * As a guide, I want to set a maximum group size and a deadline to join for my adventure, so that I can manage logistics and capacity effectively.
    * As a guide, I want to designate the adventure's difficulty level (e.g., Easy, Moderate, Strenuous), so that adventurers can accurately assess if it matches their skills.


* Feature 2: adventure discovery

    * p::1.  As an aspiring adventurer, I want to browse all adventures and see title and a brief description, so that I can get an idea of what's offered on the platform.
    * p::2.  As an aspiring adventurer, I want to view a list of adventures being offered by a specific guide, 
    * p::3.  As an aspiring adventurer, I want to search for adventures occurring within a specific date range (e.g., next weekend, next month), so that I can quickly find relevant options for my schedule.
    * p::3.  As an aspiring adventurer, I want to sort search results by "Nearest," "Date," and "Difficulty," so that I can prioritize the most relevant trips based on my immediate needs.
    --
    * As an aspiring adventurer, I want to save an adventure to a "Wishlist" without joining, so that I can easily reference it later when I am ready to book.
    * As an aspiring adventurer, I want to see how many spots are left on an adventure listing, so that I know the urgency of booking before the group fills up. 

## Story decomposition 

(do this for as many of the stories as you think will fit into your sprint)
(recommend to do RCUD order)

**Example story: Read operation**

* As a client, I want to see a list of adventures with title and description, so that..

Tasks:

* contract (see api-sketch_minimal.md):
    * minimal data model (title and description)
    * minimal API (only for this story)
* frontend: 
    * mock api_client: (read dummy data)
    * app routes: 
        - (GET /adventures/)
    * UI: adventure listing
* backend:
    * api: (read, can use dummy data for unit testing)
        - GET /adventures/
    * business logic
    * DB manager (probably already done)
* integration and deployment
    * merge frontend and backend code into main
    * integration testing
    * deployment

Example story: Create

* As a guide, I want to create an adventure with title and description, so that..

## Responsibilities

* Feature 1: Guide adventure creation
    - John (frontend)
    - Jane (backend)
* Feature 2: Adventure discovery
    - Kate (frontend)
    - Kirby (backend)

<!-- 
## Full stories

**2.1 Guide Adventure Creation**

* As a guide, I want to specify a list of required gear for my adventure, so that adventurers know what they must bring to participate.
* As a guide, I want to set a maximum group size and a deadline to join for my adventure, so that I can manage logistics and capacity effectively.
* As a guide, I want to designate the adventure's difficulty level (e.g., Easy, Moderate, Strenuous), so that adventurers can accurately assess if it matches their skills.
* As a guide, I want to mark my adventure as a "Multi-day Trip" and input start/end dates, so that users have full clarity on the commitment required.
* As a guide, I want to upload an engaging cover photo and a short video for my adventure listing, so that it attracts more interest from adventurers.
* As a guide, I want to be able to preview my adventure listing before publishing it, so that I can ensure all information is accurate and presentable.

**2.2 Adventure Discovery & Search**

* As an aspiring adventurer, I want to filter search results by the Guide's average review rating (e.g., 4 stars and up), so that I can easily find highly-rated and trustworthy experiences.
* As an aspiring adventurer, I want to search for adventures occurring within a specific date range (e.g., next weekend, next month), so that I can quickly find relevant options for my schedule.
* As an aspiring adventurer, I want to sort search results by "Nearest," "Date," and "Difficulty," so that I can prioritize the most relevant trips based on my immediate needs.
* As an aspiring adventurer, I want to view a map showing the approximate starting location for all search results, so that I can visualize the geography of my options.
* As an aspiring adventurer, I want to save an adventure to a "Wishlist" without joining, so that I can easily reference it later when I am ready to book.
* As an aspiring adventurer, I want to see how many spots are left on an adventure listing, so that I know the urgency of booking before the group fills up. -->