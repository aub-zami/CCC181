# Part 9: Accessibility Audit & Keyboard Verification

## 9a. Lighthouse
- **Join Page (`/join`):** Score: 99 / 100
- **Ticket Page (`/queue/1`):** Score: 100 / 100
- **Staff Dashboard (`/staff`):** Score: 100 / 100

*Screenshots saved in `docs/week3/screenshots/`.*

### Unfixed Issues / Notes
- All screens scored 99 or higher, far exceeding the >90 requirement. The single minor deduction on the Join page relates to a default Bootstrap minor contrast ratio suggestion that does not impact usability.

---

## 9b. Keyboard Navigation Verification
- **Home / Join Flow:** Tested using `Tab`, `Shift + Tab`, `arrow keys` and `Enter`. Form fields, service select options, and submit buttons are all reachable and visually focused.
- **My Place Flow:** "Leave the queue" button and navigation links are accessible via keyboard navigation.
- **Staff Dashboard Flow:** Action buttons ("Call Next", "Serve", "No-Show", service filter controls) are fully operable using keyboard controls alone.

---


### 9c. Manual Checklist

| Check | Join | My place | Staff |
| :--- | :---: | :---: | :---: |
| Every input has a visible label | ✅ | N/A | ✅ |
| Error messages say what to do, in text | ✅ | N/A | ✅ |
| Status is shown in words, not only color | ✅ | ✅ | ✅ |
| Text and buttons are readable at 375 px with no sideways page scroll | ✅ | ✅ | ✅ |
| Buttons are at least about 44 × 44 px on a phone | ✅ | ✅ | ✅ |
| Page has one `<h1>` and headings in order | ✅ | ✅ | ✅ |
| `<html lang="en">` (or your language) is set | ✅ | ✅ | ✅ |