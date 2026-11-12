# Synthetic incident review

A local retrieval demo failed after a fixture path changed. The browser loaded
the page, but it could no longer fetch the sample data.

| Time (UTC) | Event |
| --- | --- |
| 14:00 | Fixture moved during a refactor. |
| 14:05 | A smoke test reported a missing file. |
| 14:12 | The fixture path was corrected and the demo passed. |

The example was unavailable for twelve simulated minutes. The release check
loaded the page without exercising a query, so it missed the missing fixture.

| Follow-up | Owner role | Verification |
| --- | --- | --- |
| Submit a sample query in the release smoke test | Demo maintainer | A known query returns its expected citation. |
| Check the missing-fixture path | Test maintainer | The UI reports an actionable error. |
