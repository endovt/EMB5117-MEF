clear; clc;
node = [0 0;
        1000 2000;
        2000 0];
elem = [1 2;
        2 3];
prop = [200000 25;
        70000 16];

num_el = rows(elem);
num_no = rows(node);
f = zeros(num_no*2,1);
K = zeros(num_no*2);
Edof = zeros(num_el,4);

for i=1:num_el
  Edof(i,1) = elem(i,1)*2-1;
  Edof(i,2) = elem(i,1)*2;
  Edof(i,3) = elem(i,2)*2-1;
  Edof(i,4) = elem(i,2)*2;
end
P = 1e6;
bc = [1; 2; 5; 6];
f(4) = 10000;

for e = 1:num_el
  E = prop(e,1);
  A = prop(e,2);
  x_1 = node(elem(e,1),1);
  y_1 = node(elem(e,1),2);
  x_2 = node(elem(e,2),1);
  y_2 = node(elem(e,2),2);
  L = sqrt( (x_2-x_1)^2 + (y_2-y_1)^2 );
  c = (x_2-x_1)/L;
  s = (y_2-y_1)/L;
  T = [c s 0 0;
       0 0 c s];
  K_l = (E*A/L)*[1 -1;
                -1 1];
  K_g = T'*K_l*T;
  K(Edof(e,:),Edof(e,:)) = K(Edof(e,:),Edof(e,:)) + K_g;
end

for i=1:rows(bc)
  K(bc(i),bc(i)) = K(bc(i),bc(i))*P;
end

u = K^(-1)*f
