-- USERS (auth-managed, extended)
create table public.user_profiles (
  user_id uuid primary key references auth.users(id),
  first_name text not null,
  middle_name text,
  surname text not null,
  id_number text not null,
  id_issue_date date not null,
  created_at timestamp default now()
);

-- QUESTIONS
create table public.questions (
  id uuid primary key default gen_random_uuid(),
  text text not null,
  options text[] not null,
  correct_answer text not null,
  module_tag text
);

-- RESPONSES
create table public.responses (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id),
  question_id uuid references public.questions(id),
  answer text not null,
  submitted_at timestamp default now()
);

-- SCORES
create table public.scores (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id),
  total_score int not null,
  correct_answers int not null,
  total_questions int not null,
  passed boolean not null,
  cert_generated_at timestamp
);

-- CERTIFICATES (stateless: regeneration by hash)
create table public.certificates (
  serial_id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id),
  issued_at timestamp default now(),
  validation_name text not null,
  score_percent numeric,
  exam_version text
);

-- 🔐 RLS: Enable and isolate per-user data
alter table user_profiles enable row level security;
alter table responses enable row level security;
alter table scores enable row level security;
alter table certificates enable row level security;

create policy "Users can see their profile"
  on user_profiles for select using (auth.uid() = user_id);

create policy "Users can see their responses"
  on responses for select using (auth.uid() = user_id);

create policy "Users can see their score"
  on scores for select using (auth.uid() = user_id);

create policy "Users can view their certificates"
  on certificates for select using (auth.uid() = user_id);
