 data {
    int T;
    int T_pred;
    vector[T] TVCM;
    vector[T] Newspaper;
    vector[T] Web;
    vector[T] Y;
 }


parameters {
    vector[T] mu;
    real<lower=0> s_mu;
    real<lower=0> s_Y;
    real beta_1;
    real beta_2;
    real beta_3; 
 }

model {
    mu[2:T] ~ normal(mu[1:(T-1)], s_mu);
    Y ~ normal(mu + beta_1 * log(TVCM+1) + beta_2 * log(Newspaper+1) + beta_3 * log(Web+1), s_Y);
}


