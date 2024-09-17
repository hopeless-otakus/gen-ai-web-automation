---

title: "Explainable GI Endoscopy Procedure Assessments"
image: "https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
draft: false
filters: [making-ai-understandable, safe-ai]
researchers: ["Dr. Arun Rajkumar", "Dr. Chandrashekar Lakshmi Narayanan (RBCDSAI, IITM)", "Nithin Shivashankar (MIMYK)", Varun Seshadrinathan (MIMYK)"]
tags: ["explainable-ai", "healthcare"]
---

Gastrointestinal (GI) Endoscopy is a medical procedure wherein a trained medical expert (henceforth referred to as endoscopist) uses a flexible endoscope to examine the GI tract to screen for various diseases. Every endoscopy procedure is required to meet quality standards i.e., they need to satisfy a set of medically relevant requirements, some of which are listed below (emphasis added). In order to achieve a complete examination of the UGI tract, a standardised set of landmarks should be examined. The procedure should start at the upper oesophageal sphincter and reach the second part of the duodenum, including the upper oesophagus, gastro-oesophageal junction, fundus, gastric body, incisura, antrum, duodenal bulb and distal duodenum. The fundus should be inspected by a J-manoeuvre in all patients, and where there is a hiatus hernia the diaphragmatic pinch should be inspected while in retroflexion.

Safe performance of upper and lower endoscopy including complete navigation of the oesophagus, stomach, proximal duodenum, and colon. There are several subtle aspects of the procedure which an expert endoscopist does well (subjectively) while a trainee (who is considered as a beginner during the course of training for GI endoscopy) may not. Some key aspects:

Quality: While a well-skilled endoscopist can advance the scope into the stomach without even inflating the stomach, it is difficult for a beginner to advance the scope without air insufflation.

Compliance: A beginner should remember that the distal tip of the endoscope needs to be slightly deflected in some parts of the Oesophagus

Risk: If a diverticulum is mistaken as the lumen and the scope is advanced in that direction, there is a risk of perforation.

Real-time Adaptation: If an examinee has a vomiting reflex, the examination should be quickly done to ensure that the examinee becomes stabilised.

The project aims to develop an explainable AI model that can 'rate, understand and explain' how well an endoscopist performs an endoscopy procedure. The input to the model will be a video from a procedure performed by an endoscopist from which the model would understand 'where all did he/she look' to explain the quality of the procedure. The expected output from the model would be an 'Automated Performance Report (APR)' of the procedure along with human-understandable explanations as to how the endoscopist’s training can be improved. 