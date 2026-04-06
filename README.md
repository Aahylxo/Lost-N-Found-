🔍 Smart Lost & Found (Odoo ERP Module)
A custom Odoo module designed to digitize, automate, and streamline the Lost & Found process for university campuses or large organizations.

🎯 The Problem It Solves
Managing lost items on a busy campus is traditionally chaotic. Security staff rely on messy paper logs or disconnected spreadsheets, items pile up in storage for months, and students have no easy way to know if their belongings were ever handed in.

✨ Key Features
For Campus Security / Staff:👮
- Centralized Found Item Logging: Easily log found items with photos, locations, dates, and descriptive tags.
- Automated Tracking IDs: The system automatically generates unique, sequential reference IDs (e.g., FND/001) for every logged item to keep physical storage organized.
- Visual Kanban Dashboard: A clean, card-based Kanban view allows staff to track the status of items (Logged, Matched, Resolved, Donated) at a glance.
- Role-Based Access Control: Dedicated "Lost and Found Staff" security groups ensure only authorized personnel can resolve or donate items.
- Audit Trail & Chatter: Full integration with Odoo's internal messaging (mail.thread and mail.activity.mixin) keeps a permanent history of internal notes and status changes.

For Students / Claimants:🧑‍🎓
- Digital Claim Submission: Students can submit detailed "Lost Claims" including their contact info, item descriptions, tags, and suspected loss locations.
- Automated Email Notifications: When the system finds a match, it automatically dispatches an HTML email to the student with instructions on where to pick up their item.📩

The Auto-Match Engine (Core Logic):
Staff can trigger an intelligent matching algorithm on any submitted claim.
The engine searches the "Found" database for items that are actively logged, share common identifier tags, and have similar names.

Once a match is found, the system links the two records, updates both statuses to "Matched", and triggers the email sequence.
This module solves that by acting as a smart digital bridge. It allows staff to quickly catalog found items with photos and tags, while students submit lost claims. The system then automatically cross-references these databases to find matches and notifies the owner immediately, reducing storage clutter and reuniting students with their property faster.
Lost 'N' Found is an odoo erp system which helps in an institution where if a person loses one of their things, it minimizes the workload on a security guard who normally takes care of the lost and found item, to label, find, and recognize their owner leaving the final judgement upon the security guard. The erp system is bulletproof with what the normal students can see and what the staff can see has been put up for security purposes.
