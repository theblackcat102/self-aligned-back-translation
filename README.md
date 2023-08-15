# recreating Self-Alignment with Instruction Backtranslation

[paper](https://arxiv.org/abs/2308.06259)

High level concept is just 2 steps:

1. start with a good license LLM (but bad perf) to generate instruction based on high quality text snippet from the web

2. use the LLM to do scoring as well, basically an offline RLHF loop

## TODO

[] Use OA trainer framework to train a back translated model p(x|y) instead of p(y|x)

[] Use OA's model to setup inference server

[] Use the model create first round of instruct dataset (need to decide whether to use which web corpus). We need to include the reference corpus for offline scoring in step 2

[] Write prompts for response scoring

Bonus:

[] Extend to 2 (N) rounds conversation (seems odd no evol or instruct dataset does this), once we get a good 1st round response we could do generate the follow up questions. OASST dataset does have this knowledge

[] Viz the diversity of seed and augment data (fig 2)

