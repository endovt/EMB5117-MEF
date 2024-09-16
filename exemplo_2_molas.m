clear; clc;               % limpar memória e tela
% código rudimentar: problema 1d com dois elementos de mola em série
% -------------------------------------------------------------
% Passo 1. Obter matriz de rigidez global K
% vetor contendo a rigidez de cada mola
k_n = [10;                % rigidez da mola 1 (N/mm)
       20];               % rigidez da mola 2 (N/mm)
% cálculo do número de linhas do vetor k_n
e_total = rows(k_n);      % número total de elementos
% matriz de conectividade (graus de liberdade u_n)
dof_e = [1 2;   % elemento 1 conecta dof1 (u_1) e dof2 (u_2)
         2 3];  % elemento 2 conecta dof2 (u_2) e dof3 (u_3)
% criar matriz quadrada nula
K = zeros(3,3);           % total de dof do problema: 3
for e = 1:e_total         % loop para cada elemento
  k = k_n(e);             % rigidez do elemento (escalar)
  K_e = k*[1 -1;-1 1];    % matriz de rigidez do elemento
  % contribuição do elemento na matriz de rigidez global
  K(dof_e(e,:),dof_e(e,:)) = K(dof_e(e,:),dof_e(e,:)) + K_e;
end
display("matriz de rigidez global:"); K
% -------------------------------------------------------------
% Passo 2. Aplicação de condições de contorno
P = 1e6;                  % fator de penalização
K(1,1) = K(1,1)*P;        % penalização aplicada no termo 1,1 de K
% -------------------------------------------------------------
% Passo 3. Aplicação dos carregamentos
F = 30;                   % magnitude da força (escalar)
f = zeros(3,1);           % vetor com 3 linhas e 1 coluna
f(3) = F;                 % alterar apenas a terceira linha do vetor
display("vetor de carregamentos:"); f
% -------------------------------------------------------------
% Passo 4. Solução do sistema de equações
u = (K^-1)*f;             % resultado de deslocamentos nodais
display("vetor de deslocamentos nodais:"); u
% -------------------------------------------------------------
% Passo 5. Esboço da configuração deformada da estrutura

% -------------------------------------------------------------
% Passo 6. Aplicação de critério de falha de rigidez


