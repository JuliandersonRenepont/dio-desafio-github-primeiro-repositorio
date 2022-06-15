## Adicionar um arquivo a um repositório usando a linha de comando

Você pode enviar um arquivo existente para um repositório em GitHub.com usando a linha de comando.

**Dica:** também é possível [adicionar um arquivo existente a um repositório do site do GitHub](https://docs.github.com/pt/articles/adding-a-file-to-a-repository).

Esse procedimento pressupõe que você já:

- [Criou um repositório no GitHub](https://docs.github.com/pt/articles/creating-a-new-repository) ou tenha um repositório que pertence a outra pessoa com a qual deseja contribuir
- [Clonou o repositório localmente em seu computador](https://docs.github.com/pt/articles/cloning-a-repository)

**Aviso:** Se estiver manuseando informações confidenciais, nunca faça `git add`, `commit` ou `push` para um repositório remoto. As informações confidenciais pode incluir, entre outros:

- Senhas
- Chaves SSH
- [Chaves de acesso AWS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html)
- Chaves API
- Números de cartão de crédito
- Código PIN

Para obter mais informações, consulte "[Remover dados confidenciais do repositório](https://docs.github.com/pt/articles/removing-sensitive-data-from-a-repository)".

1. No seu computador, mova o arquivo do qual deseja fazer upload para o GitHub, no diretório local que foi criado quando o repositório foi clonado.

2. Abra Git Bash.

3. Mude o diretório de trabalho atual para o seu repositório local.

4. Faça o stage do arquivo para commit em seu repositório local.
   
   ```shell
   $ git add .
   # Adiciona o arquivo ao repositório local e faz stage dele para commit. Para remover o stage de um arquivo, use "git reset HEAD YOUR-FILE".
   ```

5. Faça o commit do arquivo em que você realizou o stage em seu repositório local.
   
   ```shell
   $ git commit -m "Add existing file"
   # Commits the tracked changes and prepares them to be pushed to a remote repository. Para remover esse commit e modificar o arquivo, use "git reset --soft HEAD~1", faça o commit e adicione o arquivo novamente.
   ```

6. [Push the changes](https://docs.github.com/pt/github/getting-started-with-github/pushing-commits-to-a-remote-repository) (Faça push das alterações</0> no seu repositório local para o GitHub.com.
   
   ```shell
   $ git push origin your-branch
   # Pushes the changes in your local repository up to the remote repository you specified as the origin
   ```
