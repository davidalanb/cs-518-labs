# Profiles - Design 

## Planning / design

Personas and stories:

* Dave - guide
    - "As Dave, I want to create a profile for my guide service, so that I can attract clients and grow my business."
    - "As Dave, I want to add my skills to my profile, so that potential clients can see my qualifications."
    - "As Dave, I want to be able to create adventures and associate them with my business."
* Jane - adventurer
    - "As Jane, I want to create a personal profile, so that I can join adventures and find adventure partners."
    - "As Jane, I want to browse adventures and see the skills required, so I can find an adventure that's right for me."
    - "As Jane, I want to sign up for an adventure, so that I can get updates and prepare."

Features:

- Setting up a profile
    - creating a profile
    - adding my skills
- Working with adventures
    - creating an adventure
    - browsing adventures 
        - (all adventures)
        - by guide / service
    - joining adventures

Data relationships:

* **User-profile**.  At first, we might want each user to have just one profile (*one-to-one*).  This simplifies things.  Later, we might want users to be able to have multiple profiles.  

* **Profile-adventure**.  A profile can be associated with many adventures (and vice-versa - *many-to-many*).
    
ERD:

* [Entity-Relationship Diagram](https://drive.google.com/file/d/1oRwl-XNePkP6AP9sSHcjhZ6qG9vKPEDu/view?usp=sharing)
