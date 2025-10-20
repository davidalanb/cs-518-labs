In general, **no**, team members should *not* all be working directly on the `main` branch during a group software engineering project. Instead, follow a **branching strategy** to keep the codebase stable and manageable.

### Recommended Workflow

1. **Protect `main` branch**
   - Require pull requests (PRs) for merging.
   - Set up required code reviews and automated tests.

2. **Each feature or bugfix gets a branch**
   - Examples:
     - `feature/login-page`
     - `bugfix/missing-validation`
   - Developers work on these branches individually or in pairs.

3. **Merge via Pull Requests**
   - When a feature is done, open a PR into `main` or `dev` (if using an intermediate `dev` branch).
   - Other team members review the code before approving and merging.

4. **Use a `dev` branch (optional but helpful)**
   - `main` = production-ready code.
   - `dev` = integration branch where all new work is merged before it’s stable enough for `main`.

---

### Why Not Work on `main` Directly?

- **Avoid breaking changes** that affect everyone.
- **Enable code review**, improving quality and knowledge sharing.
- **Support parallel development** without constant merge conflicts.

---

If you're using GitHub or GitLab, you can automate a lot of this with branch protection rules and CI.

Would you like a visual of this workflow or help setting up a branching strategy for your team?