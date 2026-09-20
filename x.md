A `LEFT JOIN` guarantees that **every single row from the left table survives** in the output, regardless of whether a matching record exists in the right table.

---

## 1. The Core Mental Model: Preservation & Padding

Think of the **left table** as your primary inventory list and the **right table** as optional supplementary details.

* **Match found:** SQL stitches the matching row from the right table directly onto the left table's row.
* **No match found:** SQL still keeps the left table's row, but generates synthetic **`NULL` values** across all columns requested from the right table.

### Concrete Example

Consider two sample tables:

**`users` (Left Table)**

| user_id | name |
| --- | --- |
| `1` | Alice |
| `2` | Bob |
| `3` | Charlie |

**`orders` (Right Table)**

| order_id | user_id | amount |
| --- | --- | --- |
| `501` | 1 | 45.00 |
| `502` | 1 | 90.00 |
| `503` | 2 | 15.00 |

*(Note: Charlie has placed zero orders. Alice has placed two.)*

---

## 2. Syntax & The Execution Pipeline

The standard syntax places the anchor table in the `FROM` clause and the supplementary table in the `LEFT JOIN` clause:

```sql
SELECT 
    users.user_id,
    users.name,
    orders.order_id,
    orders.amount
FROM users
LEFT JOIN orders 
    ON users.user_id = orders.user_id;

```

### Logical Step-by-Step Processing

1. **Establish Base (`FROM users`):** The engine loads all rows from `users`. Under no circumstance will an existing user be omitted from the output.
2. **Evaluate Join Condition (`ON users.user_id = orders.user_id`):** For each user, the engine scans `orders` to check for matching `user_id` values:
* **Alice (`user_id = 1`):** Matches orders `501` and `502`. Her row pairs with each order (producing 2 rows).
* **Bob (`user_id = 2`):** Matches order `503`. His row pairs with that order (producing 1 row).
* **Charlie (`user_id = 3`):** No match in `orders`. His row is preserved, and `orders.order_id` and `orders.amount` are filled with `NULL`.



---

## 3. The Result Set

| users.user_id | users.name | orders.order_id | orders.amount | Note |
| --- | --- | --- | --- | --- |
| `1` | Alice | `501` | `45.00` | Matched record 1 |
| `1` | Alice | `502` | `90.00` | Matched record 2 (fanout) |
| `2` | Bob | `503` | `15.00` | Matched record |
| `3` | Charlie | `NULL` | `NULL` | **Synthetic `NULL` padding** |

---

## The Golden Rules of Phase 1

* **Left-Table Row Retention:** A `LEFT JOIN` will never return fewer rows than exist in the left table. If the left table has $N$ distinct rows, the result set will contain at least $N$ rows.
* **`NULL` Signifies Absence:** In outer joins, `NULL` indicates that the `ON` condition failed to find corresponding records in the right table.
* **Fanout Occurs on Multiple Matches:** If one left row matches multiple right rows (like Alice matching two orders), the left row duplicates to pair with each match.