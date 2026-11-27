# Two pages, two dates

These fictional, one-line files disagree about the ship date of the same part.

From the repository root, run:

```sh
diff example/page-04.txt example/page-09.txt
```

Output:

```text
1c1
< The part shipped May 12.
---
> The part shipped May 21.
```

`diff` exits with status `1` because the files differ. It needs no package installation.

The source disagreement should remain visible in the draft: cite both pages and leave the date unresolved. The example demonstrates the question in [.plan](../.plan). It is a file comparison, not an automated legal workflow or a model evaluation.
