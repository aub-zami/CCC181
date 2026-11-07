# UniQueue Requirements

**Setting:** University PE Uniform Sizing, Payment, and Pickup Counter (weekday mornings)
**People who wait:** Students purchasing or picking up PE uniforms (e.g., [Juane dela Craige](week3/personas.md))
**People who serve:** PE Uniform counter staff (e.g., [Maria Claria](week3/personas.md))

**Problem statement:** A student who visits the PE uniform distribution counter between classes and endures long wait times under the sun needs a way to join a queue and track their status remotely so that they don't have to stand in the heat and won't lose their place when stepping out.

---

## 1. Functional Requirements

| ID | Requirement | Priority | Stores data? | Status |
| --- | --- | --- | --- | --- |
| FR-01 | A student can join the queue for a service by entering their name and email. | Must | **Yes** | Built (Week 3) |
| FR-02 | A student can see their ticket number, status, and how many people are ahead of them. | Must | **Yes** | Built (Week 3) |
| FR-03 | A staff member can call the next waiting ticket for a service. | Must | **Yes** | Built (Week 3) |
| FR-04 | A staff member can mark a called ticket as served or no-show. | Must | **Yes** | Built (Week 3) |
| FR-05 | A student can leave the queue before being called. | Must | **Yes** | Built (Week 3) |
| FR-06 | A student can enter their Student ID number when joining the queue. | Must | **Yes** | Built (Week 3) |
| FR-07 ★ |A staff member can add, rename, and switch off a service (e.g., Sizing, Payment, Pickup).| Must | **Yes** | This week |
| FR-08 ★ | A student can select a specific uniform size (XS, S, M, L, XL) during ticket registration. | Should | **Yes** | Later |
| FR-09 ★ | A staff member can assign or switch a ticket to a specific service counter (Counter 1 to 5). | Should | **Yes** | Later |
| FR-10 | A staff member can view daily queue analytics showing how many students were served vs no-show. | Should | **Yes** | Later |

---

## 2. Non-Functional Requirements

| ID | Requirement | Category | Priority |
| --- | --- | --- | --- |
| NFR-01 | No ticket is lost when the server or the database restarts. | Reliability | Must |
| NFR-02 | Two students can never get the same ticket number, even if they join at the exact same moment. | Data integrity | Must |
| NFR-03 | The ticket status page loads in under 2 seconds on mobile data. | Performance | Should |
| NFR-04 | Every screen scores 90 or higher in the Lighthouse accessibility check. | Accessibility | Must |
| NFR-05 | No password or secret key is stored in the Git repository. | Security | Must |

---

## 3. Scope Definition

* **MVP:** `FR-01`, `FR-02`, `FR-03`, `FR-04`, `FR-05`, `FR-06`, `FR-07`, `NFR-01`, `NFR-02`, `NFR-04`, `NFR-05`. This provides the minimum complete queue system capable of persisting ticket data reliably without losing student records during counter operation.
* **Out of scope:**
  1. *Online payment gateway integration:* Students will pay in cash or via manual counter transaction; online checkout will not be implemented this semester.
  2. *Automated SMS notification system:* Mobile text messaging updates require paid third-party API services and will be deferred.

---

## 4. Requirement Verification & Feedback

| Who (role only) | What they said | What I changed |
| --- | --- | --- |
| Student (PE Uniform Buyer) | Found the student and staff interfaces easy to navigate. Clarified how missed turns work (No-Show status requires re-queuing at the end of the line) and noted the system's clarity in monitoring served vs unserved tickets. | Validated that `FR-04` (No-Show handling) and live status tracking (`FR-02`) effectively address student confusion regarding missed turns. |s