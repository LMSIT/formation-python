# Introduction à Ansible

[Ansible](https://docs.ansible.com/) fait partie des **gestionnaires de configuration**, au même titre que:

- [Chef](https://docs.chef.io/)
- [Puppet](https://puppet.com/docs/puppet/5.5/puppet_index.html)
- [Saltstack](https://docs.saltstack.com/en/latest/contents.html)


Il ne faut pas confondre le provisionning d'infrastructure que l'on ferait avec de l'infra as code comme Terraform avec le provisionning logiciel.

Ansible, comme les autres gestionnaires de configuration est conçu pour déployer du logiciel et configurer le système, sur des machines existantes.

Terraform ou l'infra-as-code en général, sert à construire les machines et leurs dépendances (network, securité, ...)

Ansible peut aussi être utilisé pour faire de l'infra as code et construire des infrastructures mais ce n'est pas son point fort et je le déconseille fortement.

**Les particularités d'Ansible:**

- Ne demande aucune compétence en développement Python
- Tout est géré dans des fichiers de définitions YAML
- Utilise SSH et ne nécessite donc aucun agent sur la machine distante
- Ansible couvre un nombre impressionnant de cas d'usage et d'applications

**Chez Linkbynet:**

- La configuration système est géré par Chef (dns, NTP, user account, ...)
- La configuration logiciel est géré (de préférence) avec Ansible.

## Exemple de playbook Ansible

TODO...



