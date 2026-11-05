# Validation Testing Log

| Rule | Layer | How I tested it | What happened |
| :--- | :--- | :--- | :--- |
| Email must be valid | Flask | `curl -X POST http://127.0.0.1:5000/join -d "name=Test&student_id=123&email=invalidemail"` | `400 Bad Request`, flashed error "Enter a valid email address.", nothing saved |
| Name is required | Flask | `curl -X POST http://127.0.0.1:5000/join -d "name=&student_id=123&email=test@school.edu"` | `400 Bad Request`, flashed error "Enter your name (up to 80 characters).", nothing saved |
| Service must be active | Flask | `curl -X POST http://127.0.0.1:5000/join -d "name=Test&student_id=123&email=test@school.edu&service_id=999"` | `400 Bad Request`, flashed error "Please choose a valid active service.", nothing saved |
| User email must be unique | Database (UNIQUE) | `INSERT INTO users (name, email, student_id) VALUES ('Copy', 'obrenah.mendoza@g.msuiit.edu.ph', '2024-0002');` in `psql` | `ERROR: duplicate key value violates unique constraint "users_email_key" DETAIL: Key (email)=(obrenah.mendoza@g.msuiit.edu.ph) already exists.` |
| Ticket must link to existing service | Database (FOREIGN KEY) | `INSERT INTO tickets (user_id, service_id) VALUES (10, 999);` in `psql` | `ERROR: insert or update on table "tickets" violates foreign key constraint "tickets_service_id_fkey" DETAIL: Key (service_id)=(999) is not present in table "services".` |
| User name cannot be null | Database (NOT NULL) | `INSERT INTO users (name, email) VALUES (NULL, 'nullname@school.edu');` in `psql` | `ERROR: null value in column "name" of relation "users" violates not-null constraint DETAIL: Failing row contains (id, NULL, nullname@school.edu, ...).` |
| Cannot delete service with existing tickets | Database (RESTRICT) | Tried deleting service with tickets using form submission or `DELETE FROM services WHERE id=1;` | Refused by app/database: `“PE Uniform Sizing & Payment” has tickets, so it cannot be deleted. Turn it off instead.` |