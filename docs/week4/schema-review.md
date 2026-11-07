
## Review (Works Well / Problem / Change)

> **Works well:** Placing `student_id` directly in the `users` table maintains proper 3NF normalization. This ensures student identification is stored once per account rather than redundant on every created ticket.

> **Problem:** Identified through *Question 4 (Bad data)*: If a service lacks an `active` status toggle, temporarily shutting down a counter (e.g., Payment counter) would require deleting rows or causing errors on the join form.

> **Change:** Kept `active` (`boolean`, `NOT NULL DEFAULT true`) on `services` so staff can soft-disable services without deleting service history or breaking existing ticket records.

> **Works well:** Using `timestamptz` for `created_at` records timestamps in UTC down to milliseconds, allowing dynamic ordering and accurate queue calculations via `COUNT()`.

> **Problem:** Identified through *Question 3 (Facts, not results)*: Storing a `position_in_line` integer column on `tickets` would force cascading `UPDATE` queries across all waiting tickets whenever a line moves.

> **Change:** Kept `position_in_line` out of the database schema entirely, choosing instead to compute queue position dynamically on read.

> **Works well:** Foreign keys with `ON DELETE RESTRICT` guarantee audit log integrity by preventing users or staff from wiping parent records attached to past ticket entries.

> **Problem:** Identified through *Question 5 (Deletes)*: Deleting a service directly from PostgreSQL would create orphaned tickets and break end-of-day staff analytics reporting.

> **Change:** Kept `ON DELETE RESTRICT` on `tickets.service_id` and `tickets.user_id` to block deletions if historical tickets reference them.