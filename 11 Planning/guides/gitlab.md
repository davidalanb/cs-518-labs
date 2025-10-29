GitLab Setup and Execution Guide
================================

This section outlines the steps required to organize the planned work within GitLab's issue tracking and Agile tools.

I. Populate the Product Backlog (Issues)
----------------------------------------

1.  **Enter All Stories:** Navigate to **Issues** and create a separate issue for *every* selected story from the planning guide (e.g., "As a new user, I can enter my email and password...").

2.  **Add Design Tasks:** Create supplementary issues for the technical work defined in Section III of the Planning Guide (e.g., "Design and implement `User` table schema update," "Create registration API endpoint").

3.  **Labels:** Apply relevant labels to each issue:

    -   **Features:** `F1-Registration`, `F2-Profile`

    -   **Type:** `type::feature`, `type::backend`, `type::frontend`

II. Create and Scope the Iteration (Sprint)
-------------------------------------------

1.  **Create the Iteration:** Navigate to **Issues > Iterations** and create a new iteration.

    -   **Title:** e.g., "Sprint 1: User Account Core"

    -   **Dates:** Set the start and end dates (e.g., 2 weeks duration).

2.  **Assign Issues to Iteration:** Go back to the **Issue List**, select all the issues identified for this Sprint, and bulk-assign them to the newly created **Sprint 1** iteration.

III. Setup the Issue Board
--------------------------

1.  **Access the Board:** Navigate to **Issues > Boards**.

2.  **Configure:** If not already configured, ensure the board is set up with columns representing the workflow stages:

    -   **To Do / Open**

    -   **In Progress**

    -   **Review/Testing** (Crucial step for quality assurance)

    -   **Done / Closed**

3.  **Filter (Optional but Recommended):** Set the board to filter by the current **Iteration** (`Sprint 1: User Account Core`) to focus only on the committed work.

IV. Assign and Begin Work
-------------------------

1.  **Assign Issues:**

    -   Go through the issues in the **To Do** column and assign each one to the specific team member (T1, T2, T3, T4) based on the **Work Allocation** defined in the planning guide (Section IV).

2.  **Start the Sprint:** Team members move their first assigned issue from **To Do** to **In Progress** and begin development.

This setup ensures the team has a single source of truth for all work and clear ownership for the next two weeks!