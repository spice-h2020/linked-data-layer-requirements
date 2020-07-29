# Technical Requirements


This repository is meant for collecting the technical requirements for the SPICE's Linked Data Hub.

All manner of contributions are important and anyone may propose new requirements.

## Format

Requirements can be specified in natural language as [User Stories](https://en.wikipedia.org/wiki/User_story).
User stories are short descriptions of a system requirement written from the perspective of an end user of the system.
They generally have the following form:

```
[User Story Identifier] As a type-of-user, I want to some-goal (so that some-reason, optionally). 
```

For example, 

```
[InappropriateContent] As a custodian/creator, I want to identify and filter user-generated content that can be inappropriate.
```

## Guidelines for contributors

You can contribute with the collection of requirments by submitting new stories or by discussing the existing ones.
Stories are collected as issues of this repository.

Before submitting a new story please check if there already exist stories that already cover the requirement.
If not, you can submit such a story by opening a new issue and by putting the user story itself as the title.

Feel free to open new issues if you are not sure if the requirement is already covered by existing stories or you need some help for formulating the story.


## Examples of stories

This repository is meant to collect various kinds of stories. 
Here you can find some examples of the most common kinds.

#### Stories describing functional requirements (i.e. requirements describing how the system shall do)

```
[InappropriateContent] As a custodian/creator, I want to identify and filter user-generated content that can be inappropriate.
```

#### Stories describing non-functional requirements (i.e. requirements describing how the system shall be)

```
[PersistentURIs] As external developer, I want Linked Data Hub to use persistent URIs for the published resources so that published resources are stable and accessible over time.
```

#### Stories describing knowledge requirements (i.e. requirements describing what information the system shall be able to store)

```
[PerspectiveOnCulturalEntity] As a citizen, I want to express my perspective on a cultural entity, so that it is distinguished from others
```

#### Stories describing ontology alignments (i.e. requirements describing what alignments over ontology entities shall exist)

```
[EntityAlignement] As a knowledge engineer, I want to know whether different people are expressing the same concepts/facts, so that I can reason across multiple sources of knowledge.
```

#### Stories describing what knowledge shall be extracted from sources 

```
[IdentityExtraction] As a data scientist, I want to extract people names, and link them to public identities, so that I can merge/compare/enrich the knowledge about them.
````

#### Stories describing what reasoning service the system shall provide

```
[ReasoningOverCulturalEntities] As an ontology engineer, I want to perform deductive/inductive/analogical inferences over a fragment of the knowledge graph about a certain cultural object, so that implicit or hidden knowledge is materialised.
```
