# Model Card: [Model Name]

**Version**: [e.g., 1.0.0]
**Date**: [YYYY-MM-DD]
**Authors**: [Names, affiliations]
**Contact**: [Email]

---

## Model Details

### Model Description
- **Developed by**: [Organization]
- **Model type**: [e.g., Fine-tuned Llama 3.1-70B, RAG with GPT-4, Custom transformer]
- **Language(s)**: [e.g., English, multilingual]
- **License**: [e.g., MIT, Apache-2.0, Proprietary]
- **Parent model**: [If fine-tuned, name base model]
- **Resources**: [Links to paper, code, demo]

### Model Architecture
- **Base architecture**: [e.g., Decoder-only transformer, 70B parameters]
- **Modifications**: [e.g., LoRA rank-16 adapters on attention layers]
- **Context window**: [e.g., 8192 tokens]
- **Embedding model** (if RAG): [e.g., OpenAI text-embedding-ada-002]

---

## Intended Use

### Primary Uses
- **Domain**: [e.g., Legal document analysis, customer support, code generation]
- **Tasks**: [e.g., Question answering, summarization, classification]
- **Users**: [e.g., Internal employees, enterprise customers, general public]

### Out-of-Scope Uses
- **Prohibited**: [e.g., Medical diagnosis, legal advice without human review, autonomous weapon systems]
- **Not recommended**: [e.g., Sensitive personal data processing without consent]

---

## Training Data

### Data Sources
| Source | Size | Description | License |
|--------|------|-------------|---------|
| [Dataset 1] | [e.g., 100K docs] | [Internal knowledge base] | [Proprietary] |
| [Dataset 2] | [e.g., 50K examples] | [Public Q&A pairs] | [CC-BY-4.0] |

### Data Preprocessing
- **Cleaning**: [e.g., Deduplication, profanity filtering, PII removal]
- **Labeling**: [e.g., Human-labeled for relevance, RLHF feedback]
- **Augmentation**: [e.g., Back-translation for low-resource languages]

### Data Limitations
- **Bias risks**: [e.g., Over-represents English speakers, underrepresents non-binary genders]
- **Temporal coverage**: [e.g., Data current as of 2024-01; may be outdated for recent events]

---

## Training Procedure

### Training Hyperparameters
- **Epochs**: [e.g., 3]
- **Batch size**: [e.g., 32]
- **Learning rate**: [e.g., 2e-5]
- **Optimizer**: [e.g., AdamW]
- **LoRA rank** (if applicable): [e.g., 16]

### Compute Infrastructure
- **Hardware**: [e.g., 8x NVIDIA A100 80GB]
- **Training time**: [e.g., 12 hours]
- **Carbon footprint**: [e.g., 15 kg CO2e (estimated via ML CO2 Impact)]

### Training Logs
- **Experiment tracker**: [e.g., Weights & Biases run ID: abc123]
- **Loss curves**: [Link or embed chart]

---

## Evaluation

### Metrics
| Metric | Value | Benchmark |
|--------|-------|-----------|
| **Accuracy** | 87.3% | [Custom eval set (N=500)] |
| **F1 Score** | 0.85 | [SQuAD 2.0] |
| **Refusal rate** | 99.1% | [Adversarial prompts (N=100)] |
| **PII leakage** | 0% | [Golden test set (N=200)] |
| **Citation accuracy** | 94.2% | [RAG eval set (N=150)] |

### Fairness & Bias
- **Demographic parity**: Max disparity 8.2% across gender groups (within 10% threshold)
- **Equalized odds**: TPR difference 6.1% (within 10% threshold)
- **Known biases**: Slightly higher accuracy on formal language vs. colloquial speech

### Limitations
- **Hallucination rate**: 4.3% on out-of-domain queries
- **Latency**: p95 = 2.1 seconds (may be slow for real-time use)
- **Languages**: Optimized for English; degraded performance on non-English inputs

---

## Ethical Considerations

### Risks
- **Data privacy**: Training data may contain anonymized but sensitive business information
- **Misuse potential**: Could be used to generate misleading marketing content
- **Environmental**: Training consumed 15 kg CO2e (equivalent to 60 miles driven)

### Mitigations
- **Input validation**: Rejects queries for PII, credentials, or harmful content
- **Output filtering**: PII redaction layer before displaying responses
- **Human oversight**: Requires review for customer-facing outputs
- **Monitoring**: Continuous drift detection; retraining triggered if accuracy drops >5%

### Stakeholder Engagement
- **Data subjects**: [e.g., Customers notified of AI use in support interactions]
- **Affected communities**: [e.g., Legal team reviewed for discrimination risks]

---

## Deployment

### Deployment Platform
- **Infrastructure**: [e.g., AWS SageMaker, internal Kubernetes cluster]
- **Serving**: [e.g., vLLM with 4-bit quantization]
- **Access control**: [e.g., RBAC; only support-team role can query]

### Monitoring
- **Metrics tracked**: Latency, throughput, accuracy, refusal rate, PII detections
- **Alerts**: Accuracy <80%, PII leak detected, latency >5s
- **Logging**: All queries logged with user_id, timestamp, response (90-day retention)

### Update Cadence
- **Retraining schedule**: Quarterly, or triggered by drift alert
- **Version control**: Models tagged in artifact registry; rollback tested in staging

---

## Maintenance & Support

### Model Owner
- **Team**: [e.g., AI Platform Team]
- **Contact**: [ai-platform@example.com]

### Incident Response
- **Runbook**: [Link to incident response plan]
- **Escalation**: [PagerDuty rotation: ai-platform-oncall]

### Retirement Plan
- **EOL criteria**: Model accuracy <75%, or replaced by superior model
- **Data deletion**: Training data deleted 1 year post-retirement per retention policy

---

## References

### Standards & Frameworks
- **NIST AI 600-1**: Generative AI Profile (https://doi.org/10.6028/NIST.AI.600-1)
- **Model Card template**: Mitchell et al. (2019), https://arxiv.org/abs/1810.03993

### Related Artifacts
- **Risk register**: [Link]
- **SBOM**: [Link to D3 SBOM]
- **Provenance**: [Link to SLSA attestation]

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-XX | Initial release |

---

**Reviewed by**: [Governance board, legal, security]
**Approved by**: [Name, title]
**Next review**: [YYYY-MM-DD]
