FactoryGirl.define do
  factory :user do
    sequence(:name)  { |n| "Person #{n}" }
    sequence(:email) { |n| "person_#{n}@example.com"}   
    password "foobar"
    password_confirmation "foobar"

    factory :admin do
      admin true
    end
  end
  
  factory :author do
    sequence(:prefix)        { |n| "p#{n}" }
    sequence(:firstname)     { |n| "f#{n}" }
    sequence(:middlename)    { |n| "m#{n}" }  
    sequence(:lastname)      { |n| "l#{n}" }
    sequence(:suffix)        { |n| "s#{n}" }
    sequence(:birthdate)     { |n| Date.today - 20.years + n.days }
    sequence(:deathdate)     { |n| Date.today - 2.years + n.days }
    sequence(:birthdateyear) { |n| (n % 1) == 1 ? true : false }
    sequence(:deathdateyear) { |n| (n % 1) == 1 ? true : false }
    sequence(:profession)    { |n| "Job #{n mod 5}" }
  end
end
