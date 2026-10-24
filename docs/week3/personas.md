# Personas for UniQueue

## Persona 1: Juane dela Craige (The person waiting)

> "I just want to grab my uniform quickly between my morning and afternoon classes without standing under the sun for hours." *(interview)*

| Field | Details |
| --- | --- |
| **Photo or sketch** | 🙋🏻‍♂️ |
| **Age, role and background** | 17, 1st-year BET-CET student at MSU-IIT; commutes daily and has tight class schedules *(observation)*|
| **Goals** | Get PE uniform sizing done quickly; avoid missing classes; know exactly when to walk over to the counter |
| **Frustrations** | Unclear queue positions; long waiting lines in hot hallways; missing turn when leaving for a quick lunch |
| **Devices and context** | Mid-range Android smartphone (mobile data); checks phone while walking between campus buildings |
| **Tech comfort** | High — uses mobile apps daily for social media and university portals |
| **Accessibility needs** | Needs high-contrast text and clear font size to read outside in bright sunlight |

### Scenario

Juane’s assigned uniform claiming schedule is tied to his PE class time slot. When he arrives at the gym, he finds a large, crowded line made up of students from various PE sections, along with others waiting outside their designated schedule. Wanting to avoid standing under the direct heat of the sun in the unorganized queue, he opens UniQueue on his phone while walking toward the venue, selects "Uniform Claiming / Pickup", and receives Ticket #12. Seeing "4 people ahead" on his screen, he waits under the shaded bleachers nearby until his turn is called.

### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| Join queue for PE uniform claiming | Join | FR-01 |
| Check queue position and current status | My place | FR-02 |
| Leave the queue if class starts | My place | FR-03 |

### What this means for my interface

1. Because Juane checks his phone while walking in bright sunlight, his ticket number and status badge must be the largest and clearest elements on the "My place" page.
2. Because he relies on mobile data, the page must be lightweight and update automatically without requiring full page reloads.
3. Because he might need to leave suddenly, a clear "Leave queue" button must be easily accessible on his ticket page.



## Persona 2: Maria Claria (The Staff Member)

> "It gets chaotic when hundreds of freshmen arrive at once. I need a clean list so I can call the next person without yelling into the crowd."

| Field | Details |
| --- | --- |
| **Photo or sketch** | 👩🏻‍💻 |
| **Age, role and background** | 37, Administrative Staff at MSU-IIT PE Dept; handles uniform sizing, payments, and releases |
| **Goals** | Keep the line moving smoothly; easily call next student; filter queue by service type (Payment vs. Pickup) |
| **Frustrations** | Students asking "Am I next?" every minute; crowding around the counter; students missing their call |
| **Devices and context** | Office desktop laptop / counter tablet; manages queue while simultaneously checking uniform inventory |
| **Tech comfort** | Medium — comfortable with basic web browsers, spreadsheets, and university web portals |
| **Accessibility needs** | Large action buttons so she can click with a mouse or tablet touch screen without misclicking |

### Scenario

Maria Claria sits at the uniform pickup counter during peak morning hours. She opens the UniQueue Staff Dashboard on her laptop, filters the list to "Uniform Claiming / Pickup", and clicks "Call next". Ticket #12 updates to "Called", alerting Juane to approach the counter. Once she hands him the uniform, she clicks "Serve" to move to the next student.

### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| Filter active queue by service type | Staff Dashboard | FR-04 |
| Call the next waiting student | Staff Dashboard | FR-05 |
| Mark student as Served or No-Show | Staff Dashboard | FR-06 |

### What this means for my interface

1. Because Maria Claria handles high-volume desk traffic, the "Call Next" and "Serve" buttons must be prominent and easy to click with one tap.
2. Because Sizing/Payment and  Claiming occur as separate steps days apart (observation), a service filter dropdown/tabs must be placed right at the top of the dashboard.
3. Because multiple identical buttons exist in a table, every action button must have proper `aria-label` attributes for accessibility.