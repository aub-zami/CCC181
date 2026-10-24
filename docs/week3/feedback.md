# Part 3: Self-Review of Personas and Wireframes


## Screen 1: Join the Queue (`join-phone.png` & `join-laptop.png`)

- **Works well:** The form layout is simple and intuitive across mobile and desktop viewports. The vertical stack of labeled inputs allows Juane to fill out his information and request a ticket within 5 seconds.
- **Problem:** *Match between system and the real world & Error Prevention* — The "Batch No." input was confusing because students are not pre-assigned batch numbers beforehand (batches simply refer to daily release waves). Requiring students to select a batch number created unnecessary friction and risk of incorrect entries.
- **Change:** Removed the "Batch No." input from the Join form entirely to streamline ticket generation. The system automatically assigns the active batch context, while helper text was added under the "Service" dropdown to clarify counter transactions.

---

## Screen 2: My Place / Ticket (`my place-phone.png` & `my place-laptop.png`)

**Works well:** *Visibility of System Status & Visual Hierarchy* — The ticket number ("Ticket #09") and queue position ("20") are placed front-and-center in large, high-contrast typography. This directly satisfies Juane's persona rule ("Because Juane checks his phone while walking between classes in bright sunlight, his ticket number and position must be the largest element").
- **Problem:** *Minimalist Design & Data Minimization* — Displaying "Batch 2" inside the status card added visual clutter without providing actionable value to the student while waiting in line.
- **Change:** Removed the "Batch" display label from the ticket card so Juane can focus entirely on his position number ("20"), current status ("WAITING"), and estimated wait context.

---

## Screen 3: Staff Dashboard (`staff dashboard-phone.png` & `staff dasboard-laptop.png`)

- **Works well:** *Flexibility and Efficiency of Use* — The primary action button ("Call Next") is placed right above the table in a prominent layout (full-width on mobile, top-right on laptop). This allows Ate Marie to rapidly call the next student with a single tap at the counter desk.
- **Potential Risk / Problem:** *Consistency & Mobile Usability* — Displaying all candidate data columns simultaneously on small screens could clip content and make row actions hard to reach.
- **Change:** Maintained a mobile table with an explicit horizontal scroll container and a clear "table scrolls sideways" indicator from the initial wireframe phase, ensuring "Call Next" stays pinned at the top while all row actions remain accessible.