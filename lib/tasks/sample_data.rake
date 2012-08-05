namespace :db do
  desc "Fill database with sample data"
  task populate: :environment do
    # Users
    admin = User.create!(name: "Example User",
                         email: "example@railstutorial.org",
                         password: "foobar",
                         password_confirmation: "foobar")
    admin.toggle!(:admin)
    99.times do |n|
      name  = Faker::Name.name
      email = "example-#{n+1}@railstutorial.org"
      password  = "password"
      User.create!(name: name,
                   email: email,
                   password: password,
                   password_confirmation: password)
    end

    # Authors
    birthdate = Date.today - rand(0..36500).days
    deathdate = birthdate + rand(0..36500).days
    dateyear = rand( 2 ) == 1 ? true : false
    Author.create!(firstname: "Joe",
                   lastname: "Blow",
                   birthdate: birthdate,
                   deathdate: deathdate,
                   birthdateyear: dateyear,
                   deathdateyear: dateyear,
                   profession: "Actuary",
                   bio: Faker::Lorem.paragraph(3),
                   notes: Faker::Lorem.sentence(6)
                   ) 
    99.times do |n|
      name  = Faker::Name
      birthdate = Date.today - rand(0..36500).days
      deathdate = birthdate + rand(0..36500).days
      dateyear = rand( 2 ) == 1 ? true : false
      bio = Faker::Lorem.paragraph(3)
      profession = Faker::Lorem.words(1)[0].capitalize
      notes = Faker::Lorem.sentence(6)
      Author.create!(prefix: name.prefix,
                     firstname: name.first_name,
                     middlename: name.first_name,
                     lastname: name.last_name,
                     suffix: name.suffix,
                     birthdate: birthdate,
                     deathdate: deathdate,
                     birthdateyear: dateyear,
                     deathdateyear: dateyear,
                     profession: profession,
                     bio: bio,
                     notes: notes,
                     )
    end
  end
end
